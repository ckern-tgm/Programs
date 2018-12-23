describe('My First Test', function() {
  it('Visits the Page', function() {
    cy.visit('127.0.0.1:8080/')
    cy.get("#vname").type('Vorname')
    cy.get('#nname').type('Nachname')
    cy.get('#vname').contains('Vorname')
    cy.get('#nname').should('contain','Nachname')
    cy.get('#add').click()
  })
})
