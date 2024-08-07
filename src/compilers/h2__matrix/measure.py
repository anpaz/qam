from instruction_sets.h2 import instructions as h2
from instruction_sets.matrix import instructions as matrix
from qcir.circuit import Circuit, Comment, Instruction
from qstack import Handler, InstructionDefinition


class Measure(Handler):
    @property
    def source(self):
        return h2.Measure

    def uses(self) -> set[InstructionDefinition]:
        return {
            matrix.Measure,
        }

    def handle(self, inst: Instruction, _):
        return Circuit(
            self.__class__.__name__,
            [
                matrix.Measure(targets=inst.targets),
            ],
        )
