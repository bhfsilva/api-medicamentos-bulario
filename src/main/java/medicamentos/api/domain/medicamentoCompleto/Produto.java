package medicamentos.api.domain.medicamentoCompleto;

import com.google.gson.annotations.SerializedName;
import lombok.Getter;
import lombok.Setter;
import medicamentos.api.domain.categoria.Categoria;

@Getter
@Setter
public class Produto {

    String fotoMedicamentoBase64;

    @SerializedName("codigo")
    String idMedicamento;

    @SerializedName("nome")
    String nomeMedicamento;

    String numeroRegistro;

    @SerializedName("categoriaRegulatoria")
    Categoria categoria;

    String dataRegistro;

    String dataVencimentoRegistro;

    String principioAtivo;

    @SerializedName("situacaoApresentacao")
    String situacao;

    String idBulaPaciente;

    String numeroProcesso;
}
