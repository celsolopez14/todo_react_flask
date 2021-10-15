import React from 'react'


export const Card = ({listTodos, deleteTodo}) => {


    const handleDelete = (id) =>{
    
      fetch('/api/delete', {
        method: 'DELETE',
        body: JSON.stringify({
            id: id
        }),
        
    }).then(response => response.json()).then(message => {
        console.log(message)
        deleteTodo()
    })  

    }
 
    return(
        <>
        {listTodos.map(todo =>{
       return (

           <ul key = {todo.id}>
               <li>{todo.content}</li>
               <button onClick={() => handleDelete(todo.id)}>Completed</button>
           </ul>
       )     
        })}
        
        </>
    )
}