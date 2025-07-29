import ezkl
import json

def main():
    model = "iris_model.onnx"
    data = "input.json"

    print("1) Generating settings...")
    settings = ezkl.gen_settings(model=model)

    print("2) Calibrating settings with input sample...")
    settings = ezkl.calibrate_settings(model=model, settings=settings, data=data)

    print("3) Compiling model into zk circuit")
    ezkl.compile_model(model=model, compiled="iris_compiled.ezkl", settings=settings)

    print("4) Performing trusted setup")
    ezkl.setup(compiled="iris_compiled.ezkl", proving_key="pk.key", verifying_key="vk.key", settings=settings)

    print("5) Generating witness and proof")
    ezkl.gen_witness(compiled="iris_compiled.ezkl", settings=settings, witness="witness.json", data=data)
    ezkl.prove(compiled="iris_compiled.ezkl", witness="witness.json", proving_key="pk.key", proof="proof.json", settings=settings)

    print("6) Verifying proof")
    ok = ezkl.verify(proof="proof.json", verifying_key="vk.key", settings=settings)
    print("✅ Proof valid?" , ok)

if __name__ == "__main__":
    main()
