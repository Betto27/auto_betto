Feature: Fluxo de buscas

  @buscas
  Scenario: Realizar busca
    Given que acesso o site do Youtube
    And preencho o input de pesquisa
    When clico no botão de pesquisar
    Then devo visualizar os resultados da pesquisa