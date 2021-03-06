import { gql } from 'react-apollo'

export const bmcGQL = gql`
  query($id: Int!) {
    bmc(id: $id) {
      id
      name
      ip
      bmcType
      username
      password
      machines {
        id
        name
      }
    }
  }
`

export const bmcsListGQL = gql`
  {
    bmcs {
      id
      name
      ip
      bmcType
    }
  }
`

export const changeBmcGQL = gql`
  mutation changeBmc(
    $id: Int!
    $name: String!
    $bmcType: String
    $ip: String
    $username: String
    $password: String
  ) {
    changeBmc(
      id: $id
      name: $name
      bmcType: $bmcType
      ip: $ip
      username: $username
      password: $password
    ) {
      ok
      errors
      bmc {
        id
        name
      }
    }
  }
`

export const deleteBmcGQL = gql`
  mutation deleteBmc($id: Int!) {
    deleteBmc(id: $id) {
      ok
      errors
      bmc {
        id
        name
      }
    }
  }
`

export const createBmcGQL = gql`
  mutation createBmc(
    $name: String!
    $bmcType: String!
    $ip: String
    $username: String
    $password: String
  ) {
    createBmc(
      name: $name
      bmcType: $bmcType
      ip: $ip
      username: $username
      password: $password
    ) {
      ok
      errors
      bmc {
        id
        name
      }
    }
  }
`
