# This demo uses zksk (a Python library for Sigma protocols). It showcases:

# Alice (the prover) knows a secret x.

# She convinces Bob (the verifier) she knows x without revealing it.

# Similar to “I know the password that opens the cave door.”


from zksk import Secret, DLRep, utils

# Shared group generator (elliptic curve group)
g, h = utils.make_generators(num=2)

# Prover picks a secret x
x = Secret(value=42)  

# Commitment: h^x
commit = (h ** x).value  # Public commitment

# Define relation: I know x such that h^x = commit
relation = DLRep(h, commit, x)

# Prover generates non-interactive proof
proof = relation.prove()

# Verifier checks the proof
assert relation.verify(proof)
print("Proof verified: prover knows x, without revealing it.")
