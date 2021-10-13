import React from 'react'

export const Card = ({listTodos}) => {
    return(
        <>
        {listTodos.map(todo =>{
       return (
           <ul>
               <li>{todo.content}</li>
           </ul>
       )     
        })}
        
        </>
    )
}